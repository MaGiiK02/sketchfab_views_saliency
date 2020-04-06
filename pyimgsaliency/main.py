import pyimgsaliency as psal
import cv2
import glob
import numpy as np

# File related settings
DATA_PATH = './Data/**/'
FILE_FILTER = 'F_.png'
TMP_FILE_PATH = './tmp.png'

# Filter function
def calcualteSaliencyMaps(filename):
    # get the saliency maps using the 3 implemented methods
    rbd = psal.get_saliency_rbd(filename).astype('uint8')

    ft = psal.get_saliency_ft(filename).astype('uint8')

    mbd = psal.get_saliency_mbd(filename).astype('uint8')

    # often, it is desirable to have a binary saliency map
    mbd_binary_sal = psal.binarise_saliency_map(mbd,method='adaptive')
    ft_binary_sal = psal.binarise_saliency_map(ft,method='adaptive')
    rbd_binary_sal = psal.binarise_saliency_map(rbd,method='adaptive')

    return (rbd, ft, mbd, rbd_binary_sal, ft_binary_sal, mbd_binary_sal)

# File search
filenames =  glob.glob(DATA_PATH + FILE_FILTER)

#bg 
processed=1
for filename in filenames:
    (_, filepath, ext) = filename.split('.')
    ext = '.'+ext
    filepath = '.'+filepath

    original = cv2.imread(filename).astype(np.int32)
    (x, y, channels) = original.shape
    noioseArray = 4*np.random.random_sample([x,y]) - 2
    noiose = np.stack([
        noioseArray,noioseArray,noioseArray
    ],axis=2)
    tmp = (original+noiose).clip(min=0, max=255)
    cv2.imwrite(TMP_FILE_PATH,tmp.astype(np.int32))

    (rbd, ft, mbd, rbd_binary_sal, ft_binary_sal, mbd_binary_sal) = calcualteSaliencyMaps(TMP_FILE_PATH)

    # RBD-Method ()
    cv2.imwrite(
        filename=''.join([filepath,'rbd',ext]), 
        img=rbd)
    cv2.imwrite(
        filename=''.join([filepath,'rbd_binary_sal',ext]), 
        img=255 * rbd_binary_sal.astype('uint8'))

    # FT-Method ()
    cv2.imwrite(
        filename=''.join([filepath,'ft',ext]), 
        img=ft)
    cv2.imwrite(
        filename=''.join([filepath,'ft_binary_sal',ext]), 
        img=255 * ft_binary_sal.astype('uint8'))

    # MDB-method ()
    cv2.imwrite(
        filename=''.join([filepath,'mbd',ext]), 
        img=mbd)
    cv2.imwrite(
        filename=''.join([filepath,'mbd_binary_sal',ext]), 
        img=255 * mbd_binary_sal.astype('uint8'))

    print('Processed ' + filename + ' ('+str(processed)+'/'+str(len(filenames))+')')
    processed+=1
    
