import { combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux';

import flights from './flights';
import airports from './airports';
import planes from './planes';

export default combineReducers({
    routing: routerReducer,
    flights,
    airports,
    planes
});