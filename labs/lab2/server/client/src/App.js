import React, { Component } from 'react';

import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

import NavBar from './containers/NavBar';
import Router from './containers/Router';

const App = () => (
    <MuiThemeProvider>
        <div>
            <NavBar />
            <hr />
            <Router />
        </div>
    </MuiThemeProvider>
);

export default App;