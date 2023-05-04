import React from 'react';
import { Link } from 'react-router-dom';
import "./Nav.css"

function Nav() {
  return (
    <nav className="nav">
      <Link to="/" className="logo">Portal de Turismo</Link>
      <div className="search-box">
        <input type="text" placeholder="Pesquisar..." />
        <button type="submit">Buscar</button>
      </div>
      <ul className="main-menu">
        <li><Link to="/pontos-turisticos">Pontos Turísticos</Link></li>
        <li><Link to="/hoteis">Hospedagens</Link></li>
        <li><Link to="/restaurantes">Restaurantes</Link></li>
        <li><Link to="/atividades">Atividades</Link></li>
      </ul>
    </nav>
  );
}

export default Nav;
