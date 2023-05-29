import sys
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap


# 将变化后的值设置到指定的键上面
def set_map_item(follow_list, delta_map, value):
    # len of key_list must >= 1
    def get_map(key_list, follow_map):
        if len(key_list) == 1:
            return follow_map
        if not key_list[0] in follow_map.keys():
            follow_map[key_list[0]] = {}
        if len(key_list) > 1:
            new_list = key_list[1:]
            return get_map(new_list, follow_map[key_list[0]])
        else:
            return follow_map[key_list[0]]

    inner_map = get_map(follow_list, delta_map)
    inner_map[follow_list[len(follow_list) - 1]] = value


# version_value_map 原来的配置
# deploy_value_map 现在的配置
def traversal(version_value_map, deploy_value_map, follow_keys, delta_map, update_list, add_list):
    for key in deploy_value_map:
        follow_keys_copy = list(follow_keys)
        follow_keys_copy.append(key)
        # check version values if exit the same key

        if type(deploy_value_map[key]).__name__ == 'CommentedMap':
            if key in version_value_map.keys():
                if type(version_value_map[key]).__name__ == 'CommentedMap':
                    if len(version_value_map[key].keys()) == 0 and len(deploy_value_map[key].keys()) != 0:
                        # version exist and is empty
                        version_value_map[key] = deploy_value_map[key]
                        add_list.append(follow_keys_copy)
                        set_map_item(follow_keys_copy, delta_map, dict(deploy_value_map[key]))

                    else:
                        traversal(version_value_map[key], deploy_value_map[key], follow_keys_copy, delta_map,
                                  update_list, add_list)
                elif version_value_map[key] == None or type(version_value_map[key]).__name__ == 'str' or type(
                        version_value_map[key]).__name__ == 'int' or type(version_value_map[key]).__name__ == 'bool':
                    version_value_map[key] = deploy_value_map[key]
                    add_list.append(follow_keys_copy)
                    set_map_item(follow_keys_copy, delta_map, dict(deploy_value_map[key]))
            else:
                # todo
                add_list.append(follow_keys_copy)
                version_value_map[key] = deploy_value_map[key]
                set_map_item(follow_keys_copy, delta_map, dict(deploy_value_map[key]))
        elif type(deploy_value_map[key]).__name__ == 'str' or type(deploy_value_map[key]).__name__ == 'int' or type(
                deploy_value_map[key]).__name__ == 'bool' or type(
            deploy_value_map[key]).__name__ == 'PreservedScalarString' or type(
            deploy_value_map[key]).__name__ == 'FoldedScalarString' or type(
            deploy_value_map[key]).__name__ == 'LiteralScalarString':
            # check if exist
            if key in version_value_map.keys():
                if (type(deploy_value_map[key]).__name__ == 'str' or type(
                        deploy_value_map[key]).__name__ == 'int' or type(
                    deploy_value_map[key]).__name__ == 'bool' or type(
                    deploy_value_map[key]).__name__ == 'PreservedScalarString' or type(
                    deploy_value_map[key]).__name__ == 'FoldedScalarString' or type(
                    deploy_value_map[key]).__name__ == 'LiteralScalarString') and (
                        version_value_map[key] != deploy_value_map[key]):
                    # not equal,replace
                    #
                    update_list.append(follow_keys_copy)
                    version_value_map[key] = deploy_value_map[key]
                    set_map_item(follow_keys_copy, delta_map, deploy_value_map[key])
            else:
                # add new str
                add_list.append(follow_keys_copy)
                version_value_map[key] = deploy_value_map[key]
                set_map_item(follow_keys_copy, delta_map, deploy_value_map[key])
        elif type(deploy_value_map[key]).__name__ == 'CommentedSeq':
            # check if exist
            if key in version_value_map.keys():
                if type(version_value_map[key]).__name__ == 'CommentedSeq':
                    # 原数组长度为0，现在数组长度大于0，则为增加
                    if len(version_value_map[key]) == 0 and len(deploy_value_map[key]) != 0:
                        # 添加
                        add_list.append(follow_keys_copy)
                        version_value_map[key] = deploy_value_map[key]
                        set_map_item(follow_keys_copy, delta_map, deploy_value_map[key])
                    # 原来数组长度与现在数组长度不相等，且原来数组长度不为0则为更新
                    elif len(version_value_map[key]) != len(deploy_value_map[key]) and len(version_value_map[key]) != 0:
                        update_list.append(follow_keys_copy)
                        version_value_map[key] = deploy_value_map[key]
                        set_map_item(follow_keys_copy, delta_map, deploy_value_map[key])
                    # 原来数组长度与现在数组长度相等，从左往右，只要对应索引位置的元素不同则为更新
                    elif len(version_value_map[key]) == len(deploy_value_map[key]):
                        for i in range(0, len(version_value_map[key])):
                            if version_value_map[key][i] != deploy_value_map[key][i]:
                                update_list.append(follow_keys_copy)
                                version_value_map[key] = deploy_value_map[key]
                                set_map_item(follow_keys_copy, delta_map, deploy_value_map[key])
                    # 其他情况，直接视为更新
                else:
                    update_list.append(follow_keys_copy)
                    version_value_map[key] = deploy_value_map[key]
                    set_map_item(follow_keys_copy, delta_map, deploy_value_map[key])

            else:
                # add list
                add_list.append(follow_keys_copy)
                version_value_map[key] = deploy_value_map[key]
                set_map_item(follow_keys_copy, delta_map, deploy_value_map[key])
        elif type(deploy_value_map[key]).__name__ == 'NoneType':
            if key in version_value_map.keys() and type(version_value_map[key]).__name__ != 'NoneType':
                update_list.append(follow_keys_copy)
                version_value_map[key] = deploy_value_map[key]
                set_map_item(follow_keys_copy, delta_map, deploy_value_map[key])
        else:
            update_list.append(follow_keys_copy)
            version_value_map[key] = deploy_value_map[key]
            set_map_item(follow_keys_copy, delta_map, deploy_value_map[key])


def main():
    yaml = YAML()
    file_name = sys.argv[1]
    file_in = open(file_name).read()
    docs = yaml.load_all(file_in)
    i = 0
    for doc in docs:

        if i == 0:
            code_old = doc
        else:
            code_new = doc
        i = i + 1

    # 保存变化后的值,由set_map_item设置
    delta_map = CommentedMap()

    # 每一次traversal的递归遍历处理过的key,每一次递归完成回到root层时该key将会清空
    follow_keys = list()
    # 此次对比增加的key
    add = list()
    # 此次对比更新的key
    update = list()
    traversal(code_old, code_new, follow_keys, delta_map, update, add)
    yaml.dump(code_old, sys.stdout)

    split = '------love------you------choerodon------'

    print(split)
    yaml.dump(delta_map, sys.stdout)

    print(split)
    change_key_map = dict()

    change_key_map["add"] = add
    change_key_map["update"] = update
    yaml.dump(change_key_map, sys.stdout)


if __name__ == '__main__':
    main()