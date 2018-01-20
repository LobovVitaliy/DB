import React, { Component } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import axios from 'axios';

import { update } from '../redux/actions/flights';
import { get as getAirports } from '../redux/actions/airports';
import { get as getPlanes } from '../redux/actions/planes';

import Flight from '../components/Flight';

class EditFlight extends Component {
    constructor(props) {
        super(props);

        this.state = {
            flight: null
        };
    }

    componentDidMount() {
        axios.get(`/api/flights/${this.props.match.params.id}`)
            .then(res => {
                const {
                    id,
                    id_from_airport: from,
                    id_to_airport: to,
                    id_plane: plane,
                    date,
                    status
                } = res.data;
                const flight = { id, from, to, plane, date: new Date(date), status };
                this.setState({ flight })
            })
            .catch(err => console.log(err));
    }

    render() {
        return this.state.flight ? (
            <Flight {...this.props} state={this.state.flight} btn='update' />
        ) : (
            <div>Загрузка...</div>
        );
    }
}

const mapStateToProps = state => ({
    airports: state.airports,
    planes: state.planes
});

const mapDispatchToProps = dispatch => ({
    onClick: (flight) => {
        dispatch(update(flight));
    },
    actions: bindActionCreators({ getAirports, getPlanes }, dispatch)
});

export default connect(mapStateToProps, mapDispatchToProps)(EditFlight);