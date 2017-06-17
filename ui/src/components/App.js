import React from 'react'
import { BrowserRouter as Router, Route, Link } from 'react-router-dom'
import '../../static/css/App.css'
import DatasetsContainer from '../containers/DatasetsContainer'
import LabelsContainer from '../containers/LabelsContainer'

const Topic = ({ match }) => (
  <div>
    <h3>{match.params.topicId}</h3>
  </div>
)

const App = () => (
  <Router>
    <div>
      <nav className="navbar navbar-default navbar-fixed-top">
        <div className="container">
          <div className="navbar-header">
            <button type="button" className="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
              <span className="sr-only">Toggle navigation</span>
              <span className="icon-bar"></span>
              <span className="icon-bar"></span>
              <span className="icon-bar"></span>
            </button>
            <a className="navbar-brand" href="#">Project name</a>
          </div>
          <div id="navbar" className="collapse navbar-collapse">
            <ul className="nav navbar-nav">
              <li className="active"><a href="#">Home</a></li>
              <li><a href="#about">About</a></li>
              <li><a href="#contact">Contact</a></li>
            </ul>
          </div>
        </div>
      </nav>
      <div className="container">
        <Route exact path="/" component={DatasetsContainer} />
        <Route path="/:datasetName" component={LabelsContainer} />
      </div>
    </div>
  </Router>
)

export default App
