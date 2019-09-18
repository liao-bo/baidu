import APIHelper from './APIHelper';

class Sample {
    static getData() {
        return APIHelper.get(`sample/getData`, {});
    }

    static postData() {
        return APIHelper.post(`sample/postData`, null, { username: 'Jayce Tsai' });
    }

    // static putData() {
    //     return APIHelper.put(`sample/putData`, { origin: 'Jayce Tsai' }, { username: 'Jack Sparrow' });
    // }

    // static deleteDate() {
    //     return APIHelper.delete(`sample/delData`, { id: 111 });
    // }
}

export default Sample;