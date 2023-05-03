import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Homepage from './pages/Homepage';
import PontoTuristicoList from './pages/PontoTuristicoList';
//import HospedagemList from './HospedagemList';
//import RestauranteList from './RestauranteList';
//import AtividadeList from './AtividadeList';

function App() {
  return (
    <Router>
      <Homepage />
      <Switch>
        <Route path="/pontos-turisticos" component={PontoTuristicoList} />
     
      </Switch>
    </Router>
  );
}

export default App;
