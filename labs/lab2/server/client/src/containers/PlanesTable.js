import { connect } from 'react-redux';

import { get } from '../redux/actions/planes';
import PlanesTable from '../components/PlanesTable';

const mapStateToProps = state => ({ ...state.planes });

export default connect(mapStateToProps, { get })(PlanesTable);