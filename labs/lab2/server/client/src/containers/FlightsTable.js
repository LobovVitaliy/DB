import { connect } from 'react-redux';

import { get, remove } from '../redux/actions/flights';
import FlightsTable from '../components/FlightsTable';

const mapStateToProps = state => ({ ...state.flights });

export default connect(mapStateToProps, { get, remove })(FlightsTable);