export default class AniversarioService {

    constructor(resource) {

        this._resource = resource('aniversarios{/id}');
    }

    cadastra(aniversario) {

        if(aniversario._id) {

            return this._resource.update({ id: aniversario._id }, aniversario);

        } else {

            return this._resource.save(aniversario);
        }

    }

    lista() {

        return this._resource
            .query()
            .then(res => res.json(),
            err => {
                console.log(err);
                throw new Error('Não foi possível obter os aniversários no momento. Tente novamente mais tarde.');
            });
    }

    apaga(id) {

        return this._resource.delete({ id });
    }

    busca(id) {
        return this._resource.get({ id }).then(null, err => {
            console.log(err);
            throw new Error('Não foi possível remover o registro. Tente novamente mais tarde');
        });
    }
}