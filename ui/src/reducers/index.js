import { combineReducers } from 'redux'
import app from './app'
import config from './config'

const datasetApp = combineReducers({
  config,
  app,
})

export default datasetApp
