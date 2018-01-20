import React, { Component } from 'react';
import PropTypes from 'prop-types';

import SelectField from 'material-ui/SelectField';
import MenuItem from 'material-ui/MenuItem';
import DatePicker from 'material-ui/DatePicker';
import Toggle from 'material-ui/Toggle';
import RaisedButton from 'material-ui/RaisedButton';

class Flight extends Component {
    constructor(props) {
        super(props);

        this.state = props.state;
        this.handleBtnClick = this.handleBtnClick.bind(this);
    }

    componentDidMount() {
        this.props.actions.getAirports();
        this.props.actions.getPlanes();
    }

    handleChange = field => (event, index, value) => {
        this.setState({ [field]: value || index });
    }

    handleBtnClick() {
        const { from, to, plane } = this.state;
        if (from && to && plane) {
            this.props.onClick(this.state);
        }
    }

    renderMenuItems(list, field) {
        return list.map((item, i) => (
            <MenuItem value={item.id} primaryText={item[field]} key={i} />
        ));
    }

    renderSelectField(menuItems, field) {
        return (
            <SelectField
                floatingLabelText={field}
                value={this.state[field]}
                onChange={this.handleChange(field)}
            >
                {menuItems}
            </SelectField>
        );
    }

    render() {
        const style = {
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center'
        };
        const airportMenuItems = this.renderMenuItems(this.props.airports.data, 'name');
        const planeMenuItems = this.renderMenuItems(this.props.planes.data, 'id');

        return (
            <div style={style}>
                <h1>Flight</h1>
                {this.renderSelectField(airportMenuItems, 'from')}
                {this.renderSelectField(airportMenuItems, 'to')}
                {this.renderSelectField(planeMenuItems, 'plane')}
                <DatePicker
                    floatingLabelText='Date'
                    defaultDate={this.state.date}
                    onChange={this.handleChange('date')}
                />
                <Toggle
                    style={{ width: 256, marginTop: 14 }}
                    labelStyle={{ color: '#aaabae' }}
                    label='Status'
                    toggled={this.state.status ? true : false}
                    onToggle={this.handleChange('status')}
                />
                <RaisedButton
                    style={{ width: 256, marginTop: 30 }}
                    backgroundColor='#ffca00'
                    label={this.props.btn}
                    onClick={this.handleBtnClick}
                />
            </div>
        );
    }
}

Flight.propTypes = {
    onClick: PropTypes.func.isRequired,
    actions: PropTypes.object.isRequired,
    airports: PropTypes.object.isRequired,
    planes: PropTypes.object.isRequired
};

export default Flight;