manual_seed = 1
random.seed(manual_seed)
torch.manual_seed(manual_seed)
np.random.seed(manual_seed)
random.seed(manual_seed)
os.environ['PYTHONHASHSEED'] = str(0)

if torch.cuda.is_available():
	torch.cuda.manual_seed(manual_seed)
	torch.cuda.manual_seed_all(manual_seed)  
	torch.backends.cudnn.deterministic = True
	torch.backends.cudnn.benchmark = False