from PIL import Image
from random import choice

image_address = "/home/amirreza/tmp/1.jpg"
msg_address = "../Cfiles/msg.txt"

def load_image(image_address):

    im = Image.open(image_address)
    pixel = im.load()
    return pixel, im


def save_image(image_address, image):

    image.save(image_address)


def write_on_image(image_address,msg,start):
    
    choices = [-1,1]
    msg = msg[2:]
    print(msg)
    finish = 0
    p, im = load_image(image_address)
    image_size = im.size
    counter = 0
    for i in range(start[0],image_size[0]):
        for j in range(start[1],image_size[1]):
            print(counter)
            val = next(iter(msg), '-')
            if val == '-':
                return 1
            else:
                l = list(p[i,j])
                if counter <= len(msg):
                        finish = 1
                        break
                if int(msg[counter])==0 and p[i,j][0]%2==0:
                    pass
                else:
                    l[0] = l[0] + choice(choices)

                counter += 1

                if counter <= len(msg):
                        finish = 1
                        break

                if int(msg[counter])==0 and p[i,j][1]%2==0:
                    pass
                else:
                    l[1] = l[1] + choice(choices)

                counter += 1
                
                if counter <= len(msg):
                        finish = 1
                        break

                if int(msg[counter])==0 and p[i,j][2]%2==0:
                    pass
                else:
                    l[2] = l[2] + choice(choices)
                
                p[i,j] = (l[0], l[1], l[2])
                counter += 1

                if counter <= len(msg):
                        finish = 1
                        break

        else:
            if finish:
                print("finished")
                break

    save_image("/home/amirreza/tmp/22.jpg",im)
    print("saved!\a")



def read_msg(msg_address):

    msg = open(msg_address, "r")
    return msg.read()


def set_header(image_address):
    
    msg = read_msg(msg_address)
    write_on_image(image_address,str(bin(len(msg))),(0,0))



if __name__=="__main__":
    set_header(image_address)
