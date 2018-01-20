import React, { Component } from 'react';
import axios from 'axios';

import UploadPage from '../components/UploadPage';

const send = (table, file) => {
    const formData = new FormData();
    formData.append('file', file);

    const headers = {
        'Content-Type': 'multipart/form-data'
    };

    axios.post(`/api/save/${table}`, formData, { headers })
        .then(res => alert('File uploaded!'))
        .catch(err => alert(err));
};

export default () => (<UploadPage send={send} />);