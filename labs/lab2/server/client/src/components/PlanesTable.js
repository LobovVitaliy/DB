import React, { Component } from 'react';
import PropTypes from 'prop-types';

import RaisedButton from 'material-ui/RaisedButton';
import {
    Table,
    TableBody,
    TableHeader,
    TableHeaderColumn,
    TableRow,
    TableRowColumn
} from 'material-ui/Table';
import TextField from 'material-ui/TextField';
import { RadioButton, RadioButtonGroup } from 'material-ui/RadioButton';

class PlanesTable extends Component {
    constructor(props) {
        super(props);

        this.state = {
            min: '',
            max: '',
            cargo: ''
        };

        this.handleSearch = this.handleSearch.bind(this);
    }

    componentDidMount() {
        this.props.get();
    }

    renderTableRow(plane, i) {
        return (
            <TableRow key={i}>
                <TableRowColumn>{plane.id}</TableRowColumn>
                <TableRowColumn>{plane.pilot}</TableRowColumn>
                <TableRowColumn>{plane.seats}</TableRowColumn>
                <TableRowColumn>{plane.cargo.toString()}</TableRowColumn>
            </TableRow>
        );
    }

    handleChange = field => (event, value) => {
        this.setState({ [field]: value });
    }

    handleSearch() {
        this.props.get(this.state);
    }

    render() {
        return (
            <Table
                selectable={false}
                fixedHeader={false}
                style={{ tableLayout: 'auto' }}
            >
                <TableHeader
                    displaySelectAll={false}
                    adjustForCheckbox={false}
                >
                    <TableRow>
                        <TableHeaderColumn>Id</TableHeaderColumn>
                        <TableHeaderColumn>Pilot</TableHeaderColumn>
                        <TableHeaderColumn>
                            Seats
                            <TextField
                                style={{ width: 30, fontSize: 13, marginLeft: 15 }}
                                hintStyle={{ width: '100%', textAlign: 'center' }}
                                inputStyle={{ textAlign: 'center' }}
                                hintText='min'
                                onChange={this.handleChange('min')}
                            />
                            <TextField
                                style={{ width: 30, fontSize: 13, marginLeft: 15 }}
                                hintStyle={{ width: '100%', textAlign: 'center' }}
                                inputStyle={{ textAlign: 'center' }}
                                hintText='max'
                                onChange={this.handleChange('max')}
                            />
                        </TableHeaderColumn>
                        <TableHeaderColumn style={{ display: 'flex', alignItems: 'center' }}>
                            Cargo
                            <RadioButtonGroup
                                style={{ display: 'flex' }}
                                name='cargo'
                                defaultSelected={this.state.cargo}
                                onChange={this.handleChange('cargo')}
                            >
                                <RadioButton
                                    style={{ margin: '10px 20px' }}
                                    iconStyle={{ marginRight: 5 }}
                                    value={''}
                                    label='any'
                                />
                                <RadioButton
                                    style={{ margin: '10px 0' }}
                                    iconStyle={{ marginRight: 5 }}
                                    value={'true'}
                                    label='true'
                                />
                                <RadioButton
                                    style={{ margin: '10px 20px' }}
                                    iconStyle={{ marginRight: 5 }}
                                    value={'false'}
                                    label='false'
                                />
                            </RadioButtonGroup>
                            <RaisedButton
                                style={{ marginLeft: 'auto' }}
                                backgroundColor='#ffca00'
                                label='search'
                                onClick={this.handleSearch}
                            />
                        </TableHeaderColumn>
                    </TableRow>
                </TableHeader>
                <TableBody displayRowCheckbox={false}>
                    {this.props.data.map(this.renderTableRow, this)}
                </TableBody>
            </Table>
        );
    }
}

PlanesTable.propTypes = {
    get: PropTypes.func.isRequired,
    data: PropTypes.array.isRequired
};

export default PlanesTable;