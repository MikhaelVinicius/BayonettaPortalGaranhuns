
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Homepage from './pages/Homepage';
import PontoTuristicoList from './pages/PontoTuristicoList';
import AtividadeList from './pages/AtividadeList';
import Detalhes from './pages/DetalhesAtividade';
import HotelList from './pages/HotelList';
import RestauranteList from './pages/RestauranteList';
import PontoTuristicoDetalhes from './pages/DetalhesPontoTuristisco';
import HotelDetalhes from './pages/DetalhesHotel';
import RestauranteDetalhes from './pages/DetalhesRestaurante';
import EventosList from './pages/EventosList';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Homepage} />
        <Route exact path="/pontos-turisticos" component={PontoTuristicoList} />
        
        <Route path="/pontos-turisticos/:id" component={PontoTuristicoDetalhes} />
        <Route exact path="/atividades" component={AtividadeList} />
        <Route path="/atividades/:id" component={Detalhes} />
        <Route exact path="/hoteis" component={HotelList} />
        <Route path="/hoteis/:id" component={HotelDetalhes} />
        <Route exact path="/restaurantes" component={RestauranteList} />
        <Route path="/restaurantes/:id" component={RestauranteDetalhes} />
        <Route exact path="/eventos" component={EventosList} />
       
      </Switch>
    </Router>
  );
}

export default App;