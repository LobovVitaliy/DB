import axios from 'axios';

const url = '/api/flights/';

export const REQUEST_FLIGHTS = 'REQUEST_FLIGHTS';
export const GET_FLIGHTS = 'GET_FLIGHTS';
export const CREATE_FLIGHT = 'CREATE_FLIGHT';
export const UPDATE_FLIGHT = 'UPDATE_FLIGHT';
export const DELETE_FLIGHT = 'DELETE_FLIGHT';

const request = () => ({ type: REQUEST_FLIGHTS });

export const get = params => dispatch => {
    const success = data => ({ type: GET_FLIGHTS, data });

    dispatch(request());
    axios.get(url, { params })
        .then(res => dispatch(success(res.data)))
        .catch(err => console.log(err));
};

export const create = flight => dispatch => {
    const success = item => ({ type: CREATE_FLIGHT, item });

    dispatch(request());
    axios.post(url, flight)
        .then(res => dispatch(success(res.data)))
        .catch(err => console.log(err));
};

export const update = flight => dispatch => {
    const success = () => ({
        type: UPDATE_FLIGHT,
        item: {
            ...flight,
            date: flight.date.format('yyyy-mm-dd')
        }
    });

    dispatch(request());
    axios.put(url + flight.id, flight)
        .then(() => dispatch(success()))
        .catch(err => console.log(err));
};

export const remove = id => dispatch => {
    const success = () => ({ type: DELETE_FLIGHT, id });

    dispatch(request());
    axios.delete(url + id)
        .then(res => dispatch(success()))
        .catch(err => console.log(err));
};