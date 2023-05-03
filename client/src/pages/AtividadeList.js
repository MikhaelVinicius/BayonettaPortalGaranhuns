import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './AtividadeList.css';

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

  return (
    <div className="pt-list">
      <h1>Atividades</h1>
      {atividades.map(atividade => (
        <div className="pt-card" key={atividade.id}>
          <img src={atividade.imagem_url} alt={atividade.nome} />
          <div className="card-body">
            <h2>{atividade.nome}</h2>
            <p>{atividade.descricao}</p>
            <p>{atividade.localizacao}</p>
            <a href="#" className="cta-btn">Ver mais</a>
          </div>
        </div>
      ))}
    </div>
  );
}

export default AtividadeList;

