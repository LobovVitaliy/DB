import React, { Component } from 'react';
import PropTypes from 'prop-types';

import SelectField from 'material-ui/SelectField';
import MenuItem from 'material-ui/MenuItem';
import RaisedButton from 'material-ui/RaisedButton';

class UploadPage extends Component {
    constructor(props) {
        super(props);

        this.state = {
            value: 'flight',
            file: null
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleUpload = this.handleUpload.bind(this);
        this.handleSend = this.handleSend.bind(this);
    }

    handleChange(event, index, value) {
        this.setState({ value });
    }

    handleUpload(event) {
        const file = event.target.files[0] || null;
        this.setState({ file });
    }

    handleSend() {
        const { value, file } = this.state;
        if (file) {
            this.props.send(value, file);
        } else {
            alert('Error: File not found!');
        }
    }

    render() {
        const style = {
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            marginTop: 50
        };
        const file = this.state.file;
        return (
            <div style={style}>
                <SelectField
                    floatingLabelText='Select table'
                    value={this.state.value}
                    onChange={this.handleChange}
                >
                    <MenuItem value='flight' primaryText='Flight' />
                    <MenuItem value='plane' primaryText='Plane' />
                    <MenuItem value='airport' primaryText='Airport' />
                    <MenuItem value='city' primaryText='City' />
                </SelectField>
                <RaisedButton
                    style={{ width: 256,  whiteSpace: 'nowrap', overflow: 'hidden' }}
                    containerElement='label'
                    label={file ? file.name : 'file'}
                    primary={true}
                >
                    <input
                        style={{ display: 'none' }}
                        type='file'
                        onChange={this.handleUpload}
                    />
                </RaisedButton>
                <RaisedButton
                    style={{ width: 256, marginTop: 30 }}
                    labelStyle={{ color: 'white' }}
                    backgroundColor='#2abfa1'
                    label='upload'
                    onClick={this.handleSend}
                />
            </div>
        );
    }
}

UploadPage.propTypes = {
    send: PropTypes.func.isRequired
};

export default UploadPage;