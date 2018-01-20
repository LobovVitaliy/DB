import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

import RaisedButton from 'material-ui/RaisedButton';
import {
    Table,
    TableBody,
    TableHeader,
    TableHeaderColumn,
    TableRow,
    TableRowColumn
} from 'material-ui/Table';
import IconButton from 'material-ui/IconButton';
import EditorModeEdit from 'material-ui/svg-icons/editor/mode-edit';
import ActionDelete from 'material-ui/svg-icons/action/delete';

class FlightsTable extends Component {
    componentDidMount() {
        this.props.get();
    }

    renderTableRow(flight, i) {
        return (
            <TableRow key={i}>
                <TableRowColumn>{flight.id}</TableRowColumn>
                <TableRowColumn>{flight.from}</TableRowColumn>
                <TableRowColumn>{flight.to}</TableRowColumn>
                <TableRowColumn>{flight.plane}</TableRowColumn>
                <TableRowColumn>{flight.date}</TableRowColumn>
                <TableRowColumn>{flight.status.toString()}</TableRowColumn>
                <TableRowColumn style={{
                    display: 'flex',
                    justifyContent: 'space-between'
                }}>
                    <Link to={`/edit/${flight.id}`}>
                        <IconButton iconStyle={{ color: '#c200ff' }}>
                            <EditorModeEdit />
                        </IconButton>
                    </Link>
                    <IconButton
                        iconStyle={{ color: '#e00000' }}
                        onClick={() => this.props.remove(flight.id)}
                    >
                        <ActionDelete />
                    </IconButton>
                </TableRowColumn>
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
                        <TableHeaderColumn>From</TableHeaderColumn>
                        <TableHeaderColumn>To</TableHeaderColumn>
                        <TableHeaderColumn>Plane</TableHeaderColumn>
                        <TableHeaderColumn>Date</TableHeaderColumn>
                        <TableHeaderColumn>Status</TableHeaderColumn>
                        <TableHeaderColumn>
                            <Link to='/new'>
                                <RaisedButton
                                    fullWidth={true}
                                    backgroundColor='#ffca00'
                                    label='create'
                                />
                            </Link>
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

FlightsTable.propTypes = {
    get: PropTypes.func.isRequired,
    remove: PropTypes.func.isRequired,
    data: PropTypes.array.isRequired
};

export default FlightsTable;