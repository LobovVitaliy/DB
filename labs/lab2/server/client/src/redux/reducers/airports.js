import { REQUEST_AIRPORTS, GET_AIRPORTS } from '../actions/airports';

const initialState = {
    isFetching: false,
    data: []
};

export default function(state = initialState, action) {
    switch (action.type) {

        case REQUEST_AIRPORTS:
            return {
                isFetching: true,
                data: state.data
            };

        case GET_AIRPORTS:
            return {
                isFetching: false,
                data: action.data
            };

        default:
            return state;
    }
};