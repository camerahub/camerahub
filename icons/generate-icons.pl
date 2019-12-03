#!/usr/bin/perl -w

# This script generates PNG icons with the right names, at various resolutions
# from the raw SVG icons obtained from Icons8

use strict;
use warnings;

# Set up mappings between old and new icon names
my %newname = (
	'icons8-camera-addon'		=> 'accessory',
	'icons8-collectibles'		=> 'archive',
	'icons8-battery'		=> 'battery',
	'icons8-film-reel'		=> 'bulkfilm',
	'icons8-cameras'		=> 'cameramodel',
	'icons8-camera'			=> 'camera',
	'icons8-camera-identification'	=> 'condition',
	'icons8-volume'			=> 'developer',
	'icons8-industrial-scales'	=> 'enlarger',
	'icons8-easel'			=> 'exhibition',
	'icons8-medium-icons'		=> 'exposureprogram',
	'icons8-film-roll'		=> 'film',
	'icons8-360-degrees'		=> 'filter',
	'icons8-camera-flash'		=> 'flash',
	'icons8-connected-no-data'	=> 'flashprotocol',
	'icons8-resolution'		=> 'format',
	'icons8-lens'			=> 'lens',
	'icons8-factory'		=> 'manufacturer',
	'icons8-slr-small-lens'		=> 'mount',
	'icons8-metamorphose'		=> 'mountadapter',
	'icons8-movie'			=> 'negative',
	'icons8-surface'		=> 'negativesize',
	'icons8-transaction-list'	=> 'order',
	'icons8-sheets'			=> 'paperstock',
	'icons8-user'			=> 'person',
	'icons8-xlarge-icons'		=> 'print',
	'icons8-lab-items'		=> 'process',
	'icons8-screwdriver'		=> 'repair',
	'icons8-jpg'			=> 'scan',
	'icons8-diversity'		=> 'series',
	'icons8-exposure'		=> 'shutterspeed',
	'icons8-small-lens'		=> 'teleconverter',
	'icons8-test-tube'		=> 'toner',
#unknown
#login
#logout
);

# Define what resolutions we want
my @resolutions = @ARGV or die "Must specify at least one resolution";

# Define output directory
my $output = '../schema/static/icons';

# Get list of SVGs
my @files = `find svg -name '*.svg'`;

for my $resolution (@resolutions) {
	# Delete and recreate the dir
	`rm -rf $output/$resolution`;
	`mkdir $output/$resolution`;

	foreach my $file (@files) {
		chomp $file;

		# Parse filename
		$file =~ m/^svg\/(.+)-\d+\.svg$/;
		
		# If a mapping exists	
		if ($newname{$1}) {
			`convert -size ${resolution}x${resolution} $file $output/$resolution/$newname{$1}${resolution}.png`;
		}
	}
}
