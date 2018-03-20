/**
 * TODO: set up react router
 */

import React from 'react';
import ReactDOM from 'react-dom';

import {Main} from 'components/main';

const title = 'My Minimal React Webpack Babel Setup';


ReactDOM.render(
  <Main title={title} />,
  document.getElementById('app')
);
