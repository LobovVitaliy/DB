import axios from 'axios';

const url = '/api/airports/';

export const REQUEST_AIRPORTS = 'REQUEST_AIRPORTS';
export const GET_AIRPORTS = 'GET_AIRPORTS';

const request = () => ({ type: REQUEST_AIRPORTS });

export const get = () => dispatch => {
    const success = data => ({ type: GET_AIRPORTS, data });

    dispatch(request());
    axios.get(url)
        .then(res => dispatch(success(res.data)))
        .catch(err => console.log(err));
};