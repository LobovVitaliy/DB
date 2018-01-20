import { connect } from 'react-redux';

import { get } from '../redux/actions/airports';
import AirportsTable from '../components/AirportsTable';

const mapStateToProps = state => ({ ...state.airports });

export default connect(mapStateToProps, { get })(AirportsTable);