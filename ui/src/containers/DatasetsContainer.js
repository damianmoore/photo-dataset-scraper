import { connect } from 'react-redux'
import { runCommand } from '../websockets'
import Datasets from '../components/Datasets'

const mapStateToProps = (state) => {
  let sessionState = state.config.sessionState
  let datasets = []
  if (sessionState && sessionState.datasets) {
    datasets = sessionState.datasets
  }
  console.log(datasets)
  return {
    datasets: datasets,
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onClick: (id) => {
      dispatch(runCommand('get_photo_details', {id: id}))
    }
  }
}

const DatasetsContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(Datasets)

export default DatasetsContainer
