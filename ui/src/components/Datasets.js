import React, { PropTypes } from 'react'
import { Link } from 'react-router-dom'
import ProgressBar from './ProgressBar'
import { formatNumberWithCommas } from '../utils/numbers'
import '../../static/css/Datasets.css'


const Datasets = ({ datasets, onClick }) => (
  <div className="Datasets">
    <div className="page-header" id="banner">
      <div className="row">
        <div className="col-lg-8 col-md-7 col-sm-6">
          <h1>Datasets</h1>
          <p className="lead">This is them</p>
        </div>
      </div>
      <table className="table table-striped table-hover ">
        <thead>
          <tr>
            <th>Name</th>
            <th>Number of Labels</th>
            <th className="col-sm-3">Images</th>
            <th className="col-sm-3">Bottlenecks</th>
          </tr>
        </thead>
        <tbody>
          {datasets.map(dataset =>
            <tr key={dataset.name} onClick={() => onClick(dataset.name)}>
              <td><Link to={'/' + dataset.name } key={dataset.name}>{dataset.name}</Link></td>
              <td>{formatNumberWithCommas(dataset.labels.length)}</td>
              <td>
                {formatNumberWithCommas(dataset.num_images)}
                <ProgressBar percent={dataset.num_images / dataset.intended_num_images * 100} />
              </td>
              <td>
                <span>{formatNumberWithCommas(dataset.num_bottlenecks)}</span>
                <ProgressBar percent={dataset.num_bottlenecks / dataset.intended_num_images * 100} />
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  </div>
)

export default Datasets
