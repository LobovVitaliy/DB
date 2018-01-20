import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import { create } from '../redux/actions/flights';
import { get as getAirports } from '../redux/actions/airports';
import { get as getPlanes } from '../redux/actions/planes';

import Flight from '../components/Flight';

const defaultState = {
    from: null,
    to: null,
    plane: null,
    date: new Date(),
    status: 0
};

const NewFlight = props => (
    <Flight {...props} state={defaultState} btn='create' />
);

const mapStateToProps = state => ({
    airports: state.airports,
    planes: state.planes
});

const mapDispatchToProps = dispatch => ({
    onClick: (flight) => {
        dispatch(create(flight));
    },
    actions: bindActionCreators({ getAirports, getPlanes }, dispatch)
});

export default connect(mapStateToProps, mapDispatchToProps)(NewFlight);