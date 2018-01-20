import { REQUEST_PLANES, GET_PLANES } from '../actions/planes';

const initialState = {
    isFetching: false,
    data: []
};

export default function(state = initialState, action) {
    switch (action.type) {

        case REQUEST_PLANES:
            return {
                isFetching: true,
                data: state.data
            };

        case GET_PLANES:
            return {
                isFetching: false,
                data: action.data
            };

        default:
            return state;
    }
};