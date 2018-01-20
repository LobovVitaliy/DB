import { createStore, applyMiddleware, compose } from 'redux';
import { routerMiddleware } from 'react-router-redux';
import thunk from 'redux-thunk';
import reducers from './reducers';

export default history => {
    return createStore(reducers, compose(
        applyMiddleware(routerMiddleware(history), thunk),
        window.devToolsExtension ? window.devToolsExtension() : f => f
    ));
};