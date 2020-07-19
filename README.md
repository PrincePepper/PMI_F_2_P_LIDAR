# PMI_F_2_P_LIDAR

This is the median filter for Lidar that accepts strings as input. 

```one line input = one lidar snapshot.```

### work with filter
```
balance = Median_filter(step,{True from the necessity})
balance.update([10, 8, 30, 5])
```

### Sample input:

#### IN:
```
a = [[10, 8, 30, 5],
     [8, 7, 40, 3],
     [11, 10, 20, -3],
     [10, 15, 50, 2],
     [12, -3, 30, 1]]

balance.update(a[i], 5])
...
```
#### OUT:
```
[10, 8, 30, 5]
[10, 8, 40, 5]
[10, 8, 30, 3]
[10, 10, 40, 3]
[10, 8, 30, 2]
```

## __OR__
Reading data through a file, but this requires deleting:
```
a = [[10, 8, 30, 5],
     [8, 7, 40, 3],
     [11, 10, 20, -3],
     [10, 15, 50, 2],
     [12, -3, 30, 1]]
```
---------

***The project was released for my University course***

##### My contacts:
1. [Telegram](https://tgmsg.ru/princepepper)
2. [Вконтакте](https://vk.com/princepepper)
3. [Instargam](https://www.instagram.com/prince_pepper_official/?hl=ru)
4. <sereda.wk@gmail.com>
