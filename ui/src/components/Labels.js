import React, { PropTypes } from 'react'
import { Link } from 'react-router-dom'
import ProgressBar from './ProgressBar'
import { formatNumberWithCommas } from '../utils/numbers'
import '../../static/css/Labels.css'


const Labels = ({ labels, onClick }) => (
  <div className="Labels">
    <div className="page-header" id="banner">
      <div className="row">
        <div className="col-lg-8 col-md-7 col-sm-6">
          <h1>Labels</h1>
          <p className="lead">This is them</p>
        </div>
      </div>
      <table className="table table-striped table-hover ">
        <thead>
          <tr>
            <th>Name</th>
            <th className="col-sm-3">Images</th>
            <th className="col-sm-3">Bottlenecks</th>
          </tr>
        </thead>
        <tbody>
          {labels.map(label =>
            <tr key={label.name} onClick={() => onClick(label.name)}>
              <td><Link to={'/label/' + label.name } key={label.name}>{label.name}</Link></td>
              <td>
                {formatNumberWithCommas(label.num_images)}
                <ProgressBar percent={label.num_images / label.intended_num_images * 100} />
              </td>
              <td>
                <span>{formatNumberWithCommas(label.num_bottlenecks)}</span>
                <ProgressBar percent={label.num_bottlenecks / label.intended_num_images * 100} />
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  </div>
)

export default Labels
