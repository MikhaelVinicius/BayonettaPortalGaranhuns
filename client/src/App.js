
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Homepage from './pages/Homepage';
import PontoTuristicoList from './pages/PontoTuristicoList';
import AtividadeList from './pages/AtividadeList';
import Detalhes from './pages/Detalhes';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Homepage} />
        <Route path="/pontos-turisticos" component={PontoTuristicoList} />
        <Route exact path="/atividades" component={AtividadeList} />
        <Route path="/atividades/:id" component={Detalhes} />
      </Switch>
    </Router>
  );
}

export default App;