
%% A script for running saliency computation
clear all;
close all;



%% load parameters and images and set up paths
file_names = glob('./Data/**/F_.png');
mkdir './ContextAwareSaliencyOut';

%% Save the results
N = length(file_names);
for i=1:N
    file_name = file_names{i};
    splitted_filepath = strsplit(file_name, '\');
    uid = splitted_filepath(end-1);
    name = splitted_filepath(end);
    
    target_folder = cell2mat(fullfile('./ContextAwareSaliencyOut', uid))
    mkdir(target_folder);
    
    [splitted_name] = split(name, '.') 
    name_only = cell2mat(splitted_name(1))
    ext = cell2mat(splitted_name(2))
    processed_path = fullfile(target_folder, append(name_only, 'contextAware.', ext))
    copy_path = fullfile(target_folder, append(name_only, '.', ext))
    
    copyfile(file_name, copy_path);
    tmp{1} = file_name;
    processed = saliency(tmp);
    imwrite(processed{1}.SaliencyMap, processed_path);
 
end    
    
    
    