import {
    REQUEST_FLIGHTS,
    GET_FLIGHTS,
    CREATE_FLIGHT,
    UPDATE_FLIGHT,
    DELETE_FLIGHT
} from '../actions/flights';

const initialState = {
    isFetching: false,
    data: []
};

export default function(state = initialState, action) {
    switch (action.type) {

        case REQUEST_FLIGHTS:
            return {
                isFetching: true,
                data: state.data
            };

        case GET_FLIGHTS:
            return {
                isFetching: false,
                data: action.data
            };

        case CREATE_FLIGHT:
            return {
                isFetching: false,
                data: state.data.concat(action.item)
            };

        case UPDATE_FLIGHT:
            const updated = action.item;
            return {
                isFetching: false,
                data: state.data.map(item => item.id !== updated.id ? item : updated)
            };

        case DELETE_FLIGHT:
            return {
                isFetching: false,
                data: state.data.filter(item => item.id !== action.id)
            };

        default:
            return state;
    }
};