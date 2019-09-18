//app
import App from './store/App';

//增加方式，import 对应的Store模块文件
//将引用后的对象添加到return的对象中去
class StoresMap {
    static get() {
        return {
            App,
            // CP,
        }
    }
}

export default StoresMap;
