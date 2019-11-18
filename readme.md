1. 需要先安装php7.0 下载php7.0 加入环境变量
    1. mac 环境 直接执行 `brew install php@7.0`
2. 修改php.ini memory_limit = 512M #大小可根据自己内存大小调节
    1. mac下 未找到该文件 ...
3. 添加依赖 `composer`
    1. 第一次安装依赖 `composer install`
    2. 更新依赖 `composer update`
4. 反编译成js文件 $ php jsc2js.php *.jsc > test.js
4. 反汇编成js 字节码文件 $ php jsc-byte.php > test.bytecode

