
clc; clear; close all;

%% Load and Manipulate Land Area data


landData = shaperead('us4ma23m_shapefile.shp');
% disp(landData);
% depthContourData = shaperead('DEPCNT.shp');
% disp(depthContourData);

% Number of nodes you want on each boundary
numNodes = 10000;



figure(1); 
clf; 
hold on;
% Set new position and size for the figure
newPosition = [100, 100, 1200, 1000]; % [left, bottom, width, height]
set(gcf, 'Position', newPosition);

mapshow(landData);
% mapshow(depthContourData);
grid on; grid minor;



figure(2); 
clf; 
hold on;
% Set new position and size for the figure
newPosition = [200, 100, 1200, 1000]; % [left, bottom, width, height]
set(gcf, 'Position', newPosition);

%Plot the landData Shapefile data
mapshow(landData);

% Loop through each polygon in landData
for i = 1:length(landData)
    % Extract X and Y coordinates
    x = landData(i).X;
    y = landData(i).Y;
    
    % Remove NaN or Inf values
    validIndices = isfinite(x) & isfinite(y);
    x = x(validIndices);
    y = y(validIndices);
    
    % Interpolate points along the boundary
    s = linspace(0, 1, numNodes);
    xi = interp1([0 cumsum(sqrt(diff(x).^2 + diff(y).^2))], x, s, 'linear');
    yi = interp1([0 cumsum(sqrt(diff(x).^2 + diff(y).^2))], y, s, 'linear');
    
    % Plot the interpolated points
    plot(xi, yi, 'b.');
end



title('Equally Spaced Nodes on Polygon Boundaries');
grid on; grid minor;



%% Test area

% Create or select the figure
figure(3); clf; hold on;

% Set new position and size for the figure
newPosition = [100, 100, 1200, 1000]; % [left, bottom, width, height]
set(gcf, 'Position', newPosition);

% Loop through each polygon in landData
for i = 1:length(landData)
    % Display each row of landData with a different color
    % geoshow(landData(i).Y, landData(i).X, 'DisplayType', 'polygon', 'FaceColor', rand(1, 3));

    % Display each row of landData with a different color
    geoshow(landData(i).Y, landData(i).X, 'DisplayType', 'polygon', 'FaceColor',[0.824, 0.706, 0.549], 'LineWidth', 1);

    % Calculate centroid of the polygon
    centroidX = mean(landData(i).X);
    centroidY = mean(landData(i).Y);
    
    % Add a number label for index i at the centroid
    text(centroidX, centroidY, num2str(i), 'Color', 'k', 'HorizontalAlignment', 'center', 'FontSize', 100);
end



% Set up grid and other plot properties if needed
grid on; grid minor;

title('NOAA CHART DATA: US4MA23M', 'FontSize',20);












