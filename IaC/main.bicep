param location string = 'westeurope'
param appServiceAppName string = 'bookingapp${uniqueString(resourceGroup().id)}'

@allowed([
  'nonprod' 
  'prod'
])
  param environmentType string

  module appService 'modules/appService.bicep' = {
    name: 'appService'
    params: {
      location: location
      appServiceAppName: appServiceAppName
      environmentType: environmentType 
    }
  }

  output appServiceAppHostName string = appService.outputs.appServiceAppHostName
