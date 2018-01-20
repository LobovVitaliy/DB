import axios from 'axios';

const url = '/api/planes/';

export const REQUEST_PLANES = 'REQUEST_PLANES';
export const GET_PLANES = 'GET_PLANES';

const request = () => ({ type: REQUEST_PLANES });

export const get = params => dispatch => {
    const success = data => ({ type: GET_PLANES, data });

    dispatch(request());
    axios.get(url, { params })
        .then(res => dispatch(success(res.data)))
        .catch(err => console.log(err));
};