import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

import RaisedButton from 'material-ui/RaisedButton';
import SearchBar from 'material-ui-search-bar';

class NavBar extends Component {
    constructor(props) {
        super(props);

        this.state = {
            search: null,
            excluded: null
        };

        this.handleClick = this.handleClick.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.handleSearch = this.handleSearch.bind(this);
    }

    handleClick() {
        const { history, get } = this.props;
        if (history.location.pathname === '/') get();
    }

    handleChange = field => search => {
        this.setState({ [field]: search || null });
    }

    handleSearch() {
        this.props.get(this.state);
    }

    render() {
        return (
            <div style={{ display: 'flex' }}>
                <Link to='/'>
                    <RaisedButton
                        style={{ height: 48, width: 150 }}
                        label='flights'
                        primary={true}
                        onClick={this.handleClick}
                    />
                </Link>
                <SearchBar
                    style={{ width: '100%', margin: '0 25px' }}
                    hintText='Search'
                    onChange={this.handleChange('search')}
                    onRequestSearch={this.handleSearch}
                />
                <SearchBar
                    style={{ width: '100%', margin: '0 25px' }}
                    hintText='Excluded'
                    onChange={this.handleChange('excluded')}
                    onRequestSearch={this.handleSearch}
                />
                <Link to='/upload'>
                    <RaisedButton
                        style={{ height: 48, width: 150 }}
                        label='from json'
                        secondary={true}
                    />
                </Link>
            </div>
        );
    }
}

NavBar.propTypes = {
    get: PropTypes.func.isRequired
};

export default NavBar;