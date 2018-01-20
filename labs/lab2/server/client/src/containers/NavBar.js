import { withRouter } from 'react-router-dom';
import { connect } from 'react-redux';

import { get } from '../redux/actions/flights';
import NavBar from '../components/NavBar';

export default withRouter(connect(null, { get })(NavBar));