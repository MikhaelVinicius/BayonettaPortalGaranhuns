import React from 'react';
import { Link } from 'react-router-dom';

function Homepage() {
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
            <li><Link to="/pontos-turisticos">Pontos Turísticos</Link></li>
            <li><Link to="/hospedagens">Hospedagens</Link></li>
            <li><Link to="/restaurantes">Restaurantes</Link></li>
            <li><Link to="/atividades">Atividades</Link></li>
          </ul>
        </nav>
      </header>
      <main>
        <h1>Bem-vindo ao Portal de Turismo</h1>
        <p>Encontre os melhores destinos, hospedagens, restaurantes e atividades turísticas.</p>
        <Link to="/pontos-turisticos" className="cta-btn">Explorar</Link>
      </main>
      <footer>
        <ul>
          <li><Link to="/sobre">Sobre nós</Link></li>
          <li><Link to="/contato">Contato</Link></li>
          <li><Link to="/termos">Termos de uso</Link></li>
        </ul>
      </footer>
    </div>
  );
}

export default Homepage;
