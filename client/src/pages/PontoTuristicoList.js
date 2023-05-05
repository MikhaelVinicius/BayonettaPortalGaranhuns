import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './PontoTuristicoList.css';
import Nav from '../components/Nav';
import { Link } from 'react-router-dom';

function PontoTuristicoList() {
  const [pontosTuristicos, setPontosTuristicos] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/pontos_turisticos').then(response => {
        setPontosTuristicos(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  const limitarDescricao = (descricao) => {
    const limite = 200;
    if (descricao.length > limite) {
      return descricao.slice(0, limite) + '...';
    }
    return descricao;
  }

  return (
    <div className="pt-list">
       <header>
      <Nav /> 
    </header>
      <h1>Pontos turísticos</h1>
      {pontosTuristicos.map(pontoTuristico => (
        <div className="pt-card" key={pontoTuristico.id}>
          <img src={pontoTuristico.imagem_url} alt={pontoTuristico.nome} />
          <div className="card-body">
            <h2>{pontoTuristico.nome}</h2>
            <p>{limitarDescricao(pontoTuristico.descricao)}</p>
            <p>{pontoTuristico.localizacao}</p>
            <Link to={`/pontos-turisticos/${pontoTuristico.id}`} className="cta-btn">Ver mais</Link>
          </div>
        </div>
      ))}
    </div>
  );
}

export default PontoTuristicoList;
