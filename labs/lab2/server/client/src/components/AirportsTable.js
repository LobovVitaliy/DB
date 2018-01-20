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

class AirportsTable extends Component {
    componentDidMount() {
        this.props.get();
    }

    renderTableRow(airport, i) {
        return (
            <TableRow key={i}>
                <TableRowColumn>{airport.id}</TableRowColumn>
                <TableRowColumn>{airport.city}</TableRowColumn>
                <TableRowColumn>{airport.name}</TableRowColumn>
            </TableRow>
        );
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
                        <TableHeaderColumn>City</TableHeaderColumn>
                        <TableHeaderColumn>Name</TableHeaderColumn>
                    </TableRow>
                </TableHeader>
                <TableBody displayRowCheckbox={false}>
                    {this.props.data.map(this.renderTableRow, this)}
                </TableBody>
            </Table>
        );
    }
}

AirportsTable.propTypes = {
    get: PropTypes.func.isRequired,
    data: PropTypes.array.isRequired
};

export default AirportsTable;