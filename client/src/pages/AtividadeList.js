import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './AtividadeList.css';
import { Link } from 'react-router-dom';

function AtividadeList() {
  const [atividades, setAtividades] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/atividades').then(response => {
        setAtividades(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  const limitarDescricao = (descricao) => {
    const limite = 200;
    if (descricao.length <= limite) {
      return descricao;
    } else {
      return descricao.substring(0, limite) + '...';
    }
  };

  return (
    <div className="pt-list">
      <h1>Atividades</h1>
      {atividades.map(atividade => (
        <div className="pt-card" key={atividade.id}>
          <img src={atividade.imagem_url} alt={atividade.nome} />
          <div className="card-body">
            <h2>{atividade.nome}</h2>
            <p>{limitarDescricao(atividade.descricao)}</p>
            <p>{atividade.localizacao}</p>
            <Link to={`/atividades/${atividade.id}`} className="cta-btn">Ver mais</Link>
          </div>
        </div>
      ))}
    </div>
  );
}

export default AtividadeList;
