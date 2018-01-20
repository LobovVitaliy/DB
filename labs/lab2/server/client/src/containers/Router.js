import React from 'react';
import { Switch, Redirect, Route } from 'react-router-dom';

import FlightsTable from './FlightsTable';
import PlanesTable from './PlanesTable';
import AirportsTable from './AirportsTable';
import NewFlight from './NewFlight';
import EditFlight from './EditFlight';
import UploadPage from './UploadPage';

const Router = props => (
    <Switch>
        <Route exact path='/' component={FlightsTable} />
        <Route exact path='/planes' component={PlanesTable} />
        <Route exact path='/airports' component={AirportsTable} />
        <Route exact path='/new' component={NewFlight} />
        <Route exact path='/edit/:id' component={EditFlight} />
        <Route exact path='/upload' component={UploadPage} />
        <Redirect from='*' to='/' />
    </Switch>
);

export default Router;