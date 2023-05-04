import React, { useRef } from 'react';
import { Link } from 'react-router-dom';
import './Homepage.css'; 
import App from '../App';
import PontoTuristicoList from './PontoTuristicoList';
import AtividadeList from './AtividadeList';
import HotelList from './HotelList';
import RestauranteList from './RestauranteList';

function Homepage() {
  const pontoTuristicoListRef = useRef(null);
  const atividadeListRef = useRef(null);
  const hotelListRef = useRef(null);
  const restauranteListRef = useRef(null);

  const scrollToPontoTuristicoList = () => {
    pontoTuristicoListRef.current.scrollIntoView({ behavior: 'smooth' });
  };

  const scrollToAtividadeList = () => {
    atividadeListRef.current.scrollIntoView({ behavior: 'smooth' });
  };

  const scrollToHotelList = () => {
    hotelListRef.current.scrollIntoView({ behavior: 'smooth' });
  };

  const scrollToRestauranteList = () => {
    restauranteListRef.current.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <div className="homepage">
      <header>
        <nav>
          <Link to="/" className="logo">Portal de Turismo</Link>
          <div className="search-box">
            <input type="text" placeholder="Pesquisar..." />
            <button type="submit">Buscar</button>
          </div>
          <ul className="main-menu">
            <li><Link to="/pontos_turisticos"  onClick={scrollToPontoTuristicoList}>Pontos Turísticos</Link></li>
            <li><Link to="/hospedagens" onClick={scrollToHotelList}>Hospedagens</Link></li>
            <li><Link to="/restaurantes" onClick={scrollToRestauranteList}>Restaurantes</Link></li>
            <li><Link to="/atividades" onClick={scrollToAtividadeList}>Atividades</Link></li>
          </ul>
        </nav>
      </header>
      <main>
        <h1>Bem-vindo ao Portal de Turismo</h1>
        <p>Encontre os melhores destinos, hospedagens, restaurantes e atividades turísticas.</p>
        <button onClick={scrollToPontoTuristicoList} className="cta-btn">Explorar</button>
        
      </main>
      

      <div ref={pontoTuristicoListRef}>
        <PontoTuristicoList />
      </div>
      
      <div ref={atividadeListRef}>
        <AtividadeList />
      </div>

      <div ref={hotelListRef}>
        <HotelList />
      </div>

      <div ref={restauranteListRef}>
        <RestauranteList />
      </div>

    </div>
  );
}

export default Homepage;
