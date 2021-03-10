<template>
  <div class="content">
    <h2>{{ titulo }}</h2>

    <input
      type="search"
      class="filtro"
      @:input="filtro = $event.target.value"
      placeholder="Filtre pela data de aniversário"
    />
    {{ filtro }}

    <tabela-aniversario :titulo="aniversarios.nome">
      <tr v-for="aniversario of aniversariosComFiltro">
        <td>01</td>
        <td>teste</td>
        <td>21/07/1997</td>
        <td>
          <meu-botao
            rotulo="editar"
            tipo="button"
            @botaoAtivado="remove(aniversario)"
            estilo="padrao"
          />
          <meu-botao
            rotulo="remover"
            tipo="button"
            @botaoAtivado="remove(aniversario)"
            estilo="perigo"
          />
        </td>
      </tr>
    </tabela-aniversario>
  </div>
</template>

<script>
import Aniversarios from "../shared/aniversario/Aniversario.vue";
import Botao from "../shared/botao/Botao.vue";

export default {
  components: {
    "tabela-aniversario": Aniversarios,
    "meu-botao": Botao,
  },

  methods: {
    remove(aniversario) {
      if (confirm("Confirma?")) {
        alert(aniversario);
      }
    },
  },

  data() {
    return {
      titulo: "Calendário de Aniversários",
      aniversarios: [],
      filtro: "",
    };
  },

  computed: {
    aniversariosComFiltro() {
      if (this.filtro) {
        let exp = new RegExp(this.filtro.trim(), "i");
        return this.aniversarios.filter((aniversario) =>
          exp.test(aniversario.data_aniversario)
        );
      } else {
        return this.aniversarios;
      }
    },
  },

  created() {
    this.$http
      .get("https://swapi.dev/api/planets/")
      .then((res) => res.json())
      .then(
        (aniversarios) => (this.aniversarios = aniversarios),
        (err) => console.log(err)
      );
  },
};
</script>

<style>
body {
  background-color: #f2f2f2;
}

.filtro {
  display: block;
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}
</style>
