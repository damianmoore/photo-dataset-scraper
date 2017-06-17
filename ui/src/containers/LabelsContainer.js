import { connect } from 'react-redux'
import { runCommand } from '../websockets'
import Labels from '../components/Labels'

const mapStateToProps = (state, props) => {
  let sessionState = state.config.sessionState
  let labels = []
  if (sessionState && sessionState.datasets) {
    for (var dataset of sessionState.datasets) {
      if (dataset.name == props.match.params.datasetName) {
        labels = dataset.labels
      }
    }
  }
  console.log(labels)
  return {
    labels: labels,
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onClick: (id) => {
      dispatch(runCommand('get_photo_details', {id: id}))
    }
  }
}

const LabelsContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(Labels)

export default LabelsContainer
