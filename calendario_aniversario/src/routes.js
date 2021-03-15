import Cadastro from './components/cadastro/Cadastro.vue';
import Home from './components/home/Home.vue';

export const routes = [
    { path: '', name: 'home', component: Home, titulo: 'Lista de Aniversariantes', menu: true },
    { path: '/cadastro/:id', name: 'cadastro', component: Cadastro, titulo: 'Cadastrar Aniversário', menu: true },
    { path: '*', component: Home, menu: false}
];