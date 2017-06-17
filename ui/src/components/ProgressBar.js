import React, { PropTypes } from 'react'
import '../../static/css/ProgressBar.css'

const ProgressBar = ({ percent }) => (
  <div className="ProgressBar progress" title={percent + '%'}>
    <div className="progress-bar progress-bar-info" style={{width: percent + '%'}}></div>
  </div>
)

ProgressBar.propTypes = {
  percent: PropTypes.number.isRequired,
}

export default ProgressBar
